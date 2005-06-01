%define		_name	saper
%define		rel	pre7
%define		ver	0.12

Summary:	Text mode minesweeper
Summary(pl):	Saper w trybie tekstowym
Name:		fsaper
Version:	0.12%{rel}
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://marmarek.w.staszic.waw.pl/~marmarek/saper/pliki/%{_name}-current.tar.gz
# Source0-md5:	3760183322151ac9dd63a23044e6570d
Patch0:		%{name}-include.patch
URL:		http://marmarek.w.staszic.waw.pl/~marmarek/saper/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Saper is a text clone of the popular 'minesweeper' game.

%description -l pl
Tekstowy klon popularnej gry Saper (Minesweeper).

%prep
%setup -q -n %{_name}-X.%{ver}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install fsaper $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/*
